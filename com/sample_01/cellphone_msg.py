# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC1d3ed4bfac9fa9e4cc14466c6f3d95fc'
auth_token = 'c19ae506c49bdc733cc48c4e1cd42035'
client = Client(account_sid, auth_token)

message = client.messages .create(
                     body="我是测试信息",
                     from_='+17122484181',
                     to='+8617326996209'
                 )
#
# message = client.messages .create(
#                      body="今天是3.8，祝你节日快乐",
#                      from_='+8617326996209',
#                      to='+8617326996259'
#                  )

print(message.sid) #SM8e9a0c4d46824333b5ea7df0df6e07ce

print('发送者号码：',message.from_)

print('目标手机号：',message.to)
print('发送内容',message.body)

print('消息的创建时间：',message.date_created)


# 通过sid 对发送的这个短信状态查询
# updatedMessage = client.messages.get(message.sid)

# print(updatedMessage.status)


