import json
import uniout
import numpy as np
import matplotlib.pyplot as plt  # version == 2.1.2


def analysis(user_scores):
    scores = [each["score_1"] for each in user_scores]
    countries = {country_name: [each for each in user_scores if each["country"] == country_name] for country_name in set(each["country"] for each in user_scores)}
    country_info = [{"country": key, "people": len(value), "mean_score": np.mean([each["score_1"] for each in value])} for key, value in countries.items()]

    plot_data = {"country": [], "people": [], "explode": []}
    for each in sorted(country_info, key=lambda x:x["people"], reverse=True):
        sum_people = sum(plot_data["people"])
        if sum_people < 0.70 * len(user_scores):
            plot_data["country"].append(each["country"])
            plot_data["people"].append(each["people"])
            plot_data["explode"].append(0 if each["country"] != "China" else 0.1)
        else:
            plot_data["country"].append("Others")
            plot_data["people"].append(len(user_scores)-sum_people)
            plot_data["explode"].append(0)
            break
    plt.pie(plot_data["people"], explode=plot_data["explode"], labels=plot_data["country"], autopct="%3.1f%%")


with open("kickstart_user_scores.json") as fo:
    data = json.load(fo)

analysis(data)
analysis(data[:100])
analysis(data[:50])
analysis(data[1000:])