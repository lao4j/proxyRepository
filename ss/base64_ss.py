import base64

read_txt = open('heroku_ss.txt', 'rb')
read_data = read_txt.read()
read_txt.close()

base_txt = base64.b64encode(read_data)

new_run = open('heroku_ss_base64.txt', 'wb')
new_run.write(base_txt)
new_run.close()