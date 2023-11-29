from flask import Flask, render_template, request
import csv

app = Flask(__name__)
registered_Count = {}


# CSV CONVERSION SNIPPET ->
def convert_to_csv(data):
    with open("database.csv", newline="", mode="a") as database:
        teamName = data["teamName"]
        leaderName = data["leaderName"]
        member1 = data["member1"]
        member2 = data["member2"]
        member3 = data["member3"]
        leaderEmail = data["leaderEmail"]
        mobile = data["mobile"]
        psID = data["psID"]
        department = data["department"]
        problemStatementTitle = data["problemStatementTitle"]
        data_Writer = csv.writer(database, delimiter=",")
        data_Writer.writerow(
            [
                teamName,
                leaderName,
                member1,
                member2,
                member3,
                leaderEmail,
                mobile,
                psID,
                department,
                problemStatementTitle,
            ]
        )


# MAIN DRIVES ->
@app.route("/")
def home():
    print(registered_Count)
    return render_template("index.html", registered_Count=registered_Count)


@app.route("/register", methods=["POST"])
def register():
    data = request.form.to_dict()
    convert_to_csv(data)
    ps_id = data["psID"]
    if registered_Count.get(ps_id, 0) >= 2:
        return render_template("index.html", registered_Count=registered_Count)
    registered_Count[ps_id] = registered_Count.get(ps_id, 0) + 1
    return render_template(
        "confirmation.html", data=data, registered_Count=registered_Count
    )
