from postgres import fields


class CalculateStats:
    def __init__(self, raw_dict):
        self.raw_dict = raw_dict
        self.player_id = raw_dict[fields.PLAYER_ID]
        self.bat_avg = float()
        self.bowl_avg = float()
        self.total_matches = dict()
        self.result_data_dict = dict()
        self.bat_keys = list()
        self.bow_key = str()
        self.total_matches = int()
        self.generate_keys(raw_dict)

    def generate_keys(self, raw_dict):
        self.total_matches = raw_dict[fields.TOTAL_MATCHES]
        self.bat_keys = [fields.ZERO, fields.ONE, fields.TWO, fields.THREE, fields.FOURS, fields.SIX]
        self.bow_key = fields.WICKET
        return

    def calculate_bat_avg(self):
        bat_sum = 0
        for key in self.bat_keys:
            bat_sum += self.raw_dict[key]
        result = float(bat_sum) / float(self.total_matches)
        return result

    def calculate_bowl_avg(self):
        result = float(self.raw_dict[self.bow_key]) / float(self.total_matches)
        return result

    def calculate_stats(self):
        self.bat_avg = self.calculate_bat_avg()
        self.bowl_avg = self.calculate_bowl_avg()
        return

    def get_stats(self):
        self.calculate_stats()
        self.result_data_dict[fields.BATTING_AVG] = self.bat_avg
        self.result_data_dict[fields.BOWLING_AVG] = self.bowl_avg
        self.result_data_dict[fields.PLAYER_ID] = self.player_id
        return self.result_data_dict
