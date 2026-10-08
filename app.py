from flask import Flask, render_template, request

app = Flask(__name__)

ROLES = {
    "Software Developer": ["Java","Python","Data Structures","SQL","Git","REST APIs"],
    "Data Analyst": ["Python","SQL","Excel","Statistics","Data Visualization"],
    "Network Engineer": ["TCP/IP","IP Addressing","Routing","VLANs","Cisco Packet Tracer"]
}

RECOMMENDATIONS = {
    "Java":"Practice OOP, collections, exceptions and build a Java project.",
    "Python":"Practice automation, APIs and data structures.",
    "Data Structures":"Practice arrays, linked lists, stacks, queues, trees and graphs.",
    "SQL":"Practice joins, grouping, subqueries and database design.",
    "Git":"Learn branching, pull requests and collaborative workflows.",
    "REST APIs":"Build and consume APIs using Flask or Spring Boot.",
    "Excel":"Practice formulas, pivot tables and dashboards.",
    "Statistics":"Review probability, distributions, hypothesis testing and correlation.",
    "Data Visualization":"Build charts using Matplotlib or another visualization tool.",
    "TCP/IP":"Review TCP, UDP, ports, addressing and the TCP/IP model.",
    "IP Addressing":"Practice subnetting and CIDR.",
    "Routing":"Practice static routing and routing protocols.",
    "VLANs":"Practice access ports, trunking and inter-VLAN routing.",
    "Cisco Packet Tracer":"Build and troubleshoot progressively larger topologies."
}

@app.route("/", methods=["GET","POST"])
def index():
    result = None
    role = "Software Developer"
    selected = []
    if request.method == "POST":
        role = request.form.get("role", role)
        selected = request.form.getlist("skills")
        required = ROLES[role]
        missing = [s for s in required if s not in selected]
        matched = [s for s in required if s in selected]
        result = {"matched":matched,"missing":missing,
                  "recommendations":[RECOMMENDATIONS[s] for s in missing]}
    skills = sorted({s for r in ROLES.values() for s in r})
    return render_template("index.html", roles=ROLES, skills=skills,
                           result=result, role=role, selected=selected)

if __name__ == "__main__":
    app.run(debug=True)
