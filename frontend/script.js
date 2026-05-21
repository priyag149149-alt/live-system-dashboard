// LOGIN FUNCTION
async function login() {

    const username =
        document.getElementById("username").value;

    const password =
        document.getElementById("password").value;

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/login/",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    username: username,
                    password: password
                })
            }
        );

        const data = await response.json();

        console.log(data);

        if(response.ok){

            alert("Login Success");

            window.location.href =
                "dashboard.html";

        } else {

            alert(data.message);
        }

    } catch(error){

        console.log(error);

        alert("Error fetching data");
    }
}


// DASHBOARD FUNCTION
async function getStats() {

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/system/stats/"
        );

        const data = await response.json();

        console.log(data);

        document.getElementById("cpu").innerText =
            data.cpu;

        document.getElementById("memory").innerText =
            data.memory;

        document.getElementById("users").innerText =
            data.active_users;

        document.getElementById("time").innerText =
            data.server_time;

    } catch(error){

        console.log(error);
    }
}


// RUN ONLY IN DASHBOARD PAGE
if(window.location.href.includes(
    "dashboard.html"
)){

    getStats();

    setInterval(getStats, 2000);
}