import common.activity as test
import test_1_lineral.activityTest as test1
import test_2_spin.activityTest as test2
import test_3_lineral_and_spin.activityTest as test3
import test_4_move_round.activityTest as test4


def main():
    activity = test1.ActivityTest() # activity = test.Activity()
    activity.loop()


if __name__ == '__main__':
    main()
