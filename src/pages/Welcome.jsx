import React from 'react'

import { onAuthStateChanged } from 'firebase/auth';
import { auth } from '../firebase/FirebaseConfig';
import { getUserName } from '../firebase/Firestore';

import Loading from './Loading';

const Welcome = () => {


  const [currentUser, setCurrentUser] = React.useState(null);
  const [checkName,setName] = React.useState(null);
  const [UID,setUID] = React.useState(null);

  React.useEffect(() => {
    // Firebase auth listener to check for changes in user authentication status
    const unsubscribe = onAuthStateChanged(auth, (user) => {
      if (user) {

        getUserName(user.uid)
        .then(result=>
          {
            // check if name has not yet change
            if (result === "first name, last name"){

              setCurrentUser(null);
              setName(true);
              setUID(user.uid);

            }else{
              setCurrentUser(result);
              setName(null);
            }
            

          }
        )
        .catch(err=>alert(err));

      } else {
        // User is signed out
        setCurrentUser(null);
      }
    });

    // Clean up the listener when the component unmounts
    return () => unsubscribe();
  }, []);

  const UpdateName = React.lazy(() => import('./UpdateName')); // Adjust the path accordingly
  const ContinueToMain = React.lazy(() => import('./ContinueToMain')); // Adjust the path accordingly

  return (
    <div>
      <React.Suspense fallback={<Loading/>}>
        {checkName ? <UpdateName UID={UID} /> : <ContinueToMain currentUser={currentUser} />}
      </React.Suspense>
    </div>
    
  )
}

export default Welcome


