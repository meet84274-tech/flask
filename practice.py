from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def practice():
    if request.method=="POST":
        name=request.form["name"]
        password=request.form["password"]

        with open("users.txt","a") as file:
            file.write(f"{name}:{password}\n")

        return render_template("new.html",result="Australian cricket team should loose today's match")
    
    return render_template("new.html",result=" ")

if __name__ =="__main__":
    app.run(debug=True)
