class Logger:
    def __init__(self):
        self.dictionary = {}

    def shouldPrintMessage(self, timestamp, message):
        if len(self.dictionary) > 100:
            self.dictionary = {}
            print("Messages has been cleaned")

        if message not in self.dictionary:
            self.dictionary[message] = timestamp + 10
            print(f"next allowed timestamp for {message} is {timestamp}")
            print(self.dictionary)
            return True
        else:
            if timestamp >= self.dictionary[message]:
                self.dictionary[message] = timestamp + 10
                print(f"next allowed timestamp for {message} is {timestamp}")
                print(self.dictionary)
                return True
            else:
                print(timestamp, "<" ,self.dictionary[message])
                return False

    def clean(self, timestamp):
        result = True
        for key, value in self.dictionary.items():
            if value == timestamp:
                print(f"In timestamp {timestamp}, we have message {key}. That is why method will return False")
                result = False
                break
            else:
                print(f"In timestamp {timestamp}, we have no message. That is why method will return True")
                break
        return result

    def loggerSize(self):
        print(len(self.dictionary))

# Example usage
logger = Logger()

while True:
    ask = input("To add message type add, To clean type clean, To see the size of the dict type size\n")
    if ask == "add":
        t = int(input())
        m = input()
        logger.shouldPrintMessage(t, m)
    elif ask == "clean":
        t = int(input())
        logger.clean(t)
    elif ask == "size":
        logger.loggerSize()
    else:
        print("Please choose one of the three available choices")