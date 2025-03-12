import { uploadPhoto, createUser } from './utils.js';

export default function handleProfileSignup() {

  Promise.all([uploadPhoto(), createUser()])
    .then(([photo, user]) => {
      console.log(photo);
      console.log(user);
    });

  // createUser()
  //   .then((result) => console.log(`${photoBody} ${result.firstName} ${result.lastName}`));
}

