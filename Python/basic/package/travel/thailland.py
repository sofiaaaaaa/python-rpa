class ThaillandPackage:
    def detail(self):
        print("[aaaaaa] bbbb ccccc ")


if __name__ == "__main__": 
    print("Thailand 모듈 직접 실행했다.")
    trip_to = ThaillandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 실행 ")