

let monthArray = [];
let avgPriceArray = [];
let medPriceArray = [];
let yearsArray = [];
let linechart;
let monthTotalSoldArray = [];

const jsonData2 = "http://127.0.0.1:5000/api/v1.0/monthly_seattle_sales";
d3.json(jsonData2).then(function (data2) {
  for (let i = 0; i < data2.length; i++) {
    let avgPrice = data2[i]['average_sale_price'];
    let medPrice = data2[i]['median_sale_price'];
    monthArray.push(data2[i]['months']);
    avgPriceArray.push(avgPrice);
    medPriceArray.push(medPrice);
    yearsArray.push(data2[i]['years'])
    monthTotalSoldArray.push(data2[i]['total_houses_sold'])
  }
  createChart();
});

console.log(yearsArray)
console.log(monthArray)

let dateLabels = [];
for (let i = 0; i < monthArray.length; i++) {
  let monthString = String(monthArray[i]).padStart(2, '0'); // Convert to two-digit string
  let twoDigitYear = yearsArray[i].toString().slice(-2);
  dateLabels.push(monthString + '/' + twoDigitYear);
}

console.log(dateLabels);

function createChart() {
  const CHART = document.getElementById("dubLineChart").getContext('2d');
  linechart = new Chart(CHART, {
    type: 'line', // Change to line chart
    data: {
      labels: getFormattedDateLabels(monthArray, yearsArray),
      datasets: [
        {
          label: "Average Price",
          data: avgPriceArray,
          borderColor: 'green',
          backgroundColor: 'rgba(0, 255, 0, 0.2)',
          tension: 0.4,
          fill: true
        },
        {
          label: "Median Price",
          data: medPriceArray,
          borderColor: 'purple',
          backgroundColor: 'rgba(128, 0, 128, 0.2)',
          tension: 0.4,
          fill: true
        }
      ]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'top'
        },
        title: {
          display: true,
          text: 'Comparison of Average Price and Median Price'
        }
      },
      scales: {
        x: {
          type: 'category',
          position: 'bottom',
          title: {
            display: true,
            text: 'Months and Years'
          }
        },
        y: {
          title: {
            display: true,
            text: 'Price'
          }
        }
      }
    }
  });
  linechart.update();
}


function getFormattedDateLabels(monthArray, yearsArray) {
  const months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
  ];

  let dateLabels = [];
  for (let i = 0; i < monthArray.length; i++) {
    let month = months[monthArray[i] - 1];
    let year = yearsArray[i].toString().slice(-2);
    dateLabels.push(`${month}-${year}`);
  }
  return dateLabels;
}

// Add click event listener to the buttons
const avgVsMedPriceBtn = document.getElementById("AvgVsMedPrice");
avgVsMedPriceBtn.addEventListener("click", handleAvgVsMedPriceClick);

const salesVsMedPriceBtn = document.getElementById("salesVsMedPrice");
salesVsMedPriceBtn.addEventListener("click", handleSalesVsMedPriceClick);

function handleAvgVsMedPriceClick() {
  if (linechart) {
    linechart.destroy();
    createChart();
  }
}

function handleSalesVsMedPriceClick() {
  if (linechart) {
    linechart.destroy();
    createSalesVsMedPriceChart();
  }
}

function createSalesVsMedPriceChart() {
  const CHART = document.getElementById("dubLineChart").getContext('2d');
  linechart = new Chart(CHART, {
    type: 'line',
    data: {
      labels: getFormattedDateLabels(monthArray, yearsArray),
      datasets: [
        {
          label: "House Sales per Months",
          data: monthTotalSoldArray,
          borderColor: 'coral',
          backgroundColor: 'rgba(238, 130, 238, 0.2)',
          tension: 0.4,
          fill: true,
          yAxisID: 'sales-axis'
        },
        {
          label: "Median Price per Months",
          data: medPriceArray,
          borderColor: 'blue',
          backgroundColor: 'rgba(42, 213, 228, 0.2)',
          tension: 0.4,
          fill: true
        }
      ]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'top'
        },
        title: {
          display: true,
          text: 'Comparison of Change in Total House Sales and Median Price Per Month'
        }
      },
      scales: {
        x: {
          type: 'category',
          position: 'bottom',
          title: {
            display: true,
            text: 'Months and Years'
          }
        },
        y: {
          'sales-axis': {
            type: 'linear',
            beginAtZero: true,
            position: 'right'
          },
          'default': {
            type: 'linear',
            beginAtZero: true,
            position: 'left'
          }
        }
      }
    }
  });
  linechart.update();
}