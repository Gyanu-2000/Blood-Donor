document
  .getElementById("donorForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent form from reloading the page

    const name = document.getElementById("name").value;
    const bloodGroup = document.getElementById("bloodGroup").value;

    alert(
      `Thank you, ${name}! Your blood group ${bloodGroup} has been registered.`
    );

    // Optionally reset the form
    this.reset();
  });

//let url = "https://api.example.com/blood-donors";
let url = "http://127.0.0.1:5500/blood.html";
fetch(url)
  .then((response) => response.json())
  .then((data) => {
    const donorList = document.getElementById("donorList");
    data.forEach((donor) => {
      const listItem = document.createElement("li");
      listItem.textContent = `${donor.name} - ${donor.bloodGroup}`;
      donorList.appendChild(listItem);
    });
  })
  .catch((error) => console.error("Error fetching donor data:", error));

document.querySelector("section");
