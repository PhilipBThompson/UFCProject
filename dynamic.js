welcomeText = "";
const peopleData = {
    users:
        [{ name: "☕️ Fight 1  ", usageWeekly: "Heavyweight" },
        { name: "😬 Fight 2  ", usageWeekly: 13 },
        { name: "🍨 Fight 3  ", usageWeekly: 3 },
        { name: "🎸 Fight 4  ", usageWeekly: 0 },
        { name: "🚬 Fight 5  ", usageWeekly: 23 },
        { name: "🥦 Fight 6  ", usageWeekly: 7 },
        { name: "🎲 Fight 7  ", usageWeekly: 24 },
        { name: "👟 Fight 8  ", usageWeekly: 3 }]
};

//Demo of updating DOM 
const element = document.getElementById("text_input");
element.innerText = "Welcome";

//Call function with outside data 
loadElement(welcomeText)
loadJSONValues(peopleData);

function loadElement(welcomeText) {
    //const otherElement = document.getElementById("div_tag");
    //otherElement.innerText = welcomeText;
    document.getElementById("div_tag").innerText = welcomeText;
}

function loadJSONValues(boxData) {
    console.log(boxData); // Simple ckeck if getting called
    let itemName = document.getElementById("UserData");
    //Slopopy iteration of looping over list.
    for (const item of boxData.users) {
        console.log(item);
        const nodeInstance = document.createElement("ul");
        const textnode = document.createTextNode(item.name);
        const textnode2 = document.createTextNode(item.usageWeekly)
        nodeInstance.appendChild(textnode);
        nodeInstance.appendChild(textnode2)
        itemName.appendChild(nodeInstance);
    }


}

let newsFeed = APICallFetchData(); //returns JS object from JSON data

function APICallFetchData() {
    //Call other service (on AWWS cloud with different URL to fetch data)
    //expects JSON returned with dat, otherwise handle errors
    //convert it to javascript object for ease
    //you call it and it returns below
}
/* Set the width of the side navigation to 250px */
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

/* Set the width of the side navigation to 0 */
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}