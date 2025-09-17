import clicker,time
import hand_tracking_base as htb

clicker = clicker.Clicker(cooldown=1.0)

def main():
    for i in range(5):
        time.sleep(1)
        clicker.click()


if __name__ == "__main__":
    main()