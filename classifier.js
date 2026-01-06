function calculateEarlyVelocity(i5, i15, i30) {
  return i30 - i5;
}

function calculateEngagementRatio(likes, replies, reposts, i30) {
  if (i30 === 0) return 0;
  return (likes + replies + reposts) / i30;
}

function classify() {
  const i5 = Number(document.getElementById("i5").value);
  const i15 = Number(document.getElementById("i15").value);
  const i30 = Number(document.getElementById("i30").value);
  const likes = Number(document.getElementById("likes").value);
  const replies = Number(document.getElementById("replies").value);
  const reposts = Number(document.getElementById("reposts").value);

  const velocity = calculateEarlyVelocity(i5, i15, i30);
  const ratio = calculateEngagementRatio(likes, replies, reposts, i30);

  let state;
  if (velocity > 500 && ratio > 0.02) {
    state = "GREEN";
  } else if (velocity > 100) {
    state = "YELLOW";
  } else {
    state = "RED";
  }

  const resultEl = document.getElementById("result");
resultEl.className = `result ${state}`;
resultEl.innerHTML = `
  <div class="state">${state}</div>
  <div><strong>Early Velocity:</strong> ${velocity}</div>
  <div><strong>Engagement Ratio:</strong> ${ratio.toFixed(3)}</div>
`;
}