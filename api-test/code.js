// To run this assignment, right click on index.html in the Visual Studio file explorer to the left
// and select "Open with Live Server"

// Your Code Here.

let userLocation = {
  latitude: 0,
  longitude: 0 
};

function updateUserLocation(position) {
  userLocation.latitude = position.coords.latitude;
  userLocation.longitude = position.coords.longitude;
  console.log(userLocation.latitude, userLocation.longitude);
}

function handleLocationError(error) {
  console.log(error.message);
 
  const errorMessage = 'Could not access user location. Using default location.';
  console.log(errorMessage);
 
  userLocation = {
    latitude: 40.7829, 
    longitude: -73.9654 
  };
}

if (navigator.geolocation) {
  navigator.geolocation.watchPosition(updateUserLocation, handleLocationError);
} else {
  console.log('Geolocation is not supported by this browser.');
  handleLocationError({ message: 'Geolocation is not supported.' });
}

const apiKey = '85be07821197b2a917c62918e58e508f'; 
const proxyUrl = 'http://shrouded-mountain-15003.herokuapp.com/';
const apiUrl = 'http://api.flickr.com/services/rest/';

function constructQueryUrl(latitude, longitude, searchTerm) {
  const params = new URLSearchParams({
    api_key: apiKey,
    format: 'json',
    nojsoncallback: 1,
    method: 'flickr.photos.search',
    safe_search: 1,
    per_page: 6,
    lat: latitude,
    lon: longitude,
    text: searchTerm
  });

  const url = new URL(apiUrl);
  url.search = params.toString();

  return proxyUrl + url.toString();
}

function fetchPhotos(queryUrl) {
  fetch(queryUrl)
    .then(response => response.json())
    .then(data => {
     
      console.log(data); 
    })
    .catch(error => {
      console.log('Error:', error);
      
    });
}

const queryUrl = constructQueryUrl(userLocation.latitude, userLocation.longitude, 'cat');
console.log(queryUrl); 

fetchPhotos(queryUrl);
