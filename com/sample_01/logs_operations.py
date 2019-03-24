import  logging

logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s- %(message)s')

logging.debug('start my programme')

logging.info('test')


def factorial(n):

    logging.debug('start of factorial(%s%%)' %(n))

    total = 1

    for i in range(n+1):

        total *=i

        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))

    return  total

print(factorial(2))

logging.debug('End of programme')



### 将日志记录到文件 ，只需要指定日志文件记录接口

logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


