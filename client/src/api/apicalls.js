import axios from 'axios';

async function registerUser({ name, cardsPerDay }) {
  axios
    .post('/auth/register', {
      name: name,
      cards_per_day: cardsPerDay,
    })
    .then(function (response) {
      console.log(`registerUser ${response}`);
    })
    .catch(function (error) {
      console.log(error);
    });
}
async function loginUser({ name, cardsPerDay }) {
  axios
    .post('/auth/login', {
      name: name,
    })
    .then(function (response) {
      console.log(`loginUser ${response}`);
    })
    .catch(function (error) {
      console.log(error);
    });
}
export { registerUser, loginUser };
