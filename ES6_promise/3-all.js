import uploadPhoto from './utils.js';
import createUser from './utils.js';

export default function handleProfileSignup() {
  const uploadPhotoPromise = Promise.resolve();
  const createUserPromise = Promise.resolve();
  let photoBody;

  uploadPhotoPromise
    .then((result) => {
      console.log(result);
      // photoBody = result.body;
    });

  // createUserPromise
  //   .then((result) => console.log(`${photoBody} ${result.firstName} ${result.lastName}`));
}

