// script.js
async function setup() {
  try {
    const response = await fetch('timetable.json');
    if (!response.ok) throw new Error('Failed to fetch JSON');
    const data = await response.json();

    function starting() {
      console.clear();
      console.log("Starting function called");

      let vsv = false;
      let day = 0;     // Change as needed
      let period = 1;

      try {
        const periodData = data.data.dates[day].periods[period];

        if (periodData.timetables[0].description) {
          // VSV period case
          const ClassName = periodData.programs[0].name;
          const ClassRoom = periodData.programs[0].room_name;
          console.log(`VSV Class: ${ClassName}, Room: ${ClassRoom}`);
          vsv = true;
        } else if (day !== 5 && period < 6 && !vsv) {
          // Regular class
          const ClassName = periodData.className;
          const ClassRoom = periodData.timetables[0].timetable.roomlist;
          console.log(`Class: ${ClassName}, Room: ${ClassRoom}`);
        } else {
          console.log("Not a valid day or period");
        }
      } catch (err) {
        console.error("Error accessing timetable data:", err);
      }
    }

    document.getElementById('myButton').addEventListener('click', starting);
  } catch (error) {
    console.error('Error loading JSON:', error);
  }
}

setup();
