class Head:
    def __init__(self):
        self.eyes = 2
        self.ears = 2
        self.nose = 1
        self.mouth = 1


class Hand:
    def __init__(self):
        self.fingers = 5


class Arm:
    def __init__(self, hand: Hand):
        self.hand = hand


class Feet:
    def __init__(self):
        self.toes = 5


class Leg:
    def __init__(self, foot: Feet):
        self.foot = foot


class Torso:
    def __init__(self, head: Head, left_arm: Arm, right_arm: Arm, left_leg: Leg, right_leg: Leg):
        self.head = head
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.left_leg = left_leg
        self.right_leg = right_leg


class Human:
    def __init__(self):
        head = Head()

        left_hand = Hand()
        right_hand = Hand()

        left_arm = Arm(left_hand)
        right_arm = Arm(right_hand)

        left_foot = Feet()
        right_foot = Feet()

        left_leg = Leg(left_foot)
        right_leg = Leg(right_foot)

        self.torso = Torso(
            head,
            left_arm,
            right_arm,
            left_leg,
            right_leg
        )

    def describe(self):
        return {
            "eyes": self.torso.head.eyes,
            "ears": self.torso.head.ears,
            "nose": self.torso.head.nose,
            "mouth": self.torso.head.mouth,
            "fingers_left": self.torso.left_arm.hand.fingers,
            "fingers_right": self.torso.right_arm.hand.fingers,
            "toes_left": self.torso.left_leg.foot.toes,
            "toes_right": self.torso.right_leg.foot.toes
        }


human = Human()

print(human.describe())