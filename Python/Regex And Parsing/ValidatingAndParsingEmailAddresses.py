import email.utils
import re

pattern = re.compile(r"^[a-zA-Z][\w\-.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$")
for _ in range(int(input())):
  u_name, u_email = email.utils.parseaddr(input())
  if pattern.match(u_email):
    print(email.utils.formataddr((u_name, u_email)))