url = "https://www.youtube.com/watch?v=kWiCuklohdY&t=4801s"
my = url.replace("https://","")
my = my[:my.index(".")]
passward = my[:3] + str(len(my)) + str(my.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(url, passward))
