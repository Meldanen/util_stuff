import copy
import datetime
import random


class Rota:

    def __init__(self, users, options):
        self.user_option_pairs = [(a, b) for a in users for b in options if a != b]
        self.pairinos = self.getPairinos(len(options))
        self.finalement = self.getFinalement()

    def getPairinos(self, offset):
        current_user = []
        pairinos = []
        for i in range(0, len(self.user_option_pairs), offset):
            for j in range(offset):
                current_user.append(self.user_option_pairs[i + j])
            pairinos.append(current_user)
            current_user = []
        return pairinos

    def findStuff(self, pairs):
        fail_count = 0
        candidate_pair = []
        final_pairs = []
        el_pairos = copy.deepcopy(pairs)
        el_pairos_size = len(el_pairos)
        for i in range(el_pairos_size):
            for j in range(el_pairos_size):
                while len(candidate_pair) < el_pairos_size:
                    if i == 0:
                        candidate_pair = [("Alex", "Ftino Revisit"), ("Ninos", "Kenurgio"), ("Despo", "Revisit"), ("Evi", "Ftino Kenurgio"), ("Kalia", "Karakiozis")]
                    if fail_count > 100:
                        return "fail"
                    if len(el_pairos[j]) - 1 < 0:
                        return "fail"
                    index = random.randint(0, len(el_pairos[j]) - 1)
                    el_pairo = el_pairos[j][index]
                    if self.isOptionAlreadyInThisWeek(candidate_pair, el_pairo):
                        fail_count += 1
                        continue
                    else:
                        candidate_pair.append(el_pairo)
                        j += 1
            final_pairs.append(candidate_pair)
            for el_pairo in el_pairos:
                for pair in candidate_pair:
                    if pair in el_pairo:
                        el_pairo.remove(pair)
            candidate_pair = []
        return final_pairs

    def getFinalement(self):
        finalement = "fail"
        while finalement == "fail":
            random.shuffle(self.pairinos)
            finalement = self.findStuff(self.pairinos)
        return finalement

    def print(self):
        weekCount = 0
        day_offset = 7
        start_date = datetime.date.today() + datetime.timedelta(days=-1)
        print("-----New rota thingie-----")
        # random.shuffle(self.finalement)
        for i, pair in enumerate(self.finalement):
            if i > 0:
                random.shuffle(pair)
            for j, item in enumerate(pair):
                if weekCount > 0 and weekCount % len(users) == 0 and weekCount != (len(users) * len(options)):
                    print("-----New rota thingie-----")
                current_week = start_date + datetime.timedelta(days=day_offset*weekCount)
                next_week = start_date + datetime.timedelta(days=day_offset*(weekCount+1)-1)
                print(f'{current_week.strftime("%d/%m/%y")}-{next_week.strftime("%d/%m/%y")} : Week {weekCount + 1}: {item}')

                weekCount += 1

    @staticmethod
    def isOptionAlreadyInThisWeek(candidate_pair, user_option_pair):
        for (user, option) in candidate_pair:
            if option == user_option_pair[1]:
                return True
        return False


users = ["Alex", "Despo", "Evi", "Kalia", "Ninos"]
options = ["Kenurgio", "Revisit", "Ftino Kenurgio", "Ftino Revisit", "Karakiozis"]
rota = Rota(users, options)
rota.print()

