import { Avatar, Button, Grid ,Stack, Typography} from '@mui/material'
import defaultImage from "../../Images/logo512.png"
import React from 'react'
import { statusLogin } from '../../firebase/FirebaseConfig'
import { getUserDetails } from '../../firebase/Firestore'
import { LogoutSession } from '../../Authentication/Authentication'
import ProfileSettings from '../admin/ProfileSettings'

const Settings = () => {
    const [image,setImage] = React.useState(defaultImage) //image

    const [showChange,setShowChange] = React.useState(true)

    const [name, setName] = React.useState({
        uid: "",
        email: "",
        firstName: "",
        lastName: ""
      });

    // get username in firestore
    React.useEffect(()=>{
    let isMounted = true;

    const fetchUserStatus = async () => {
      try {
        const user = await statusLogin();
        if (isMounted) {

          const details = await getUserDetails(user.uid)

          const [lastName, firstName] = details.user.split(",");
          setName({
            uid:user.uid,
            email: user.email,
            firstName: firstName,
            lastName: lastName
          });

          details.photoUrl ? setImage(details.photoUrl) : setImage(image)

        }
      } catch (error) {
        console.error('Error fetching user status:', error);
      }
    };

    fetchUserStatus();

    return () => {
      isMounted = false;
    };
    },[])

return (
    <div>
    {showChange ? 
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>

        <Grid 
        container   
        direction="row"
        justifyContent="center"
        alignItems="flex-start"
        spacing={0}
        marginTop={20}
        paddingX={1}
        style={{ 
            minHeight: "100vh"
        }}
        >
            <Grid item xs={12} md={5} sm={12} 
            sx={{ padding: '30px' }}>

                <Stack 
                spacing={2}   
                direction="column"
                justifyContent="center"
                alignItems="center">

                    {/* Profile Settings */}
                    <div
                    style={{
                        width: '200px',
                        height: '200px',
                        border: '2px solid rgb(61, 152, 154)',
                        borderRadius: "50%",
                        position: 'relative',
                        cursor: 'pointer',
                    }}
                    >
                        <Avatar src={image} sx={{ width: '100%', height: '100%' }}>
                        A
                        </Avatar>
                    </div>

                    {/* Full Name */}
                    <Stack 
                    direction="column"
                    justifyContent="center"
                    alignItems="center">

                        <Typography variant='h5' color="black" fontWeight="bold" fontSize="1.3rem">
                            {String(name.firstName + " " + name.lastName).toUpperCase()} 
                        </Typography>

                        <Typography variant='h5' color="black" fontWeight="lighter" fontSize="0.9rem">
                            {name.email}
                        </Typography>
                    </Stack>


                    {/* Change Password */}
                    <Button
                    fullWidth
                    variant="contained"
                    color="primary" // You can adjust the color based on your design
                    style={{
                        marginTop: '20px', // Add some spacing from the elements above
                        borderRadius: '10px', // Add rounded corners for a modern look
                    }}
                    onClick={()=>setShowChange(false)}
                    >
                        Change Password
                    </Button>
                    
                    {/* Log Out */}
                    <Button
                    fullWidth
                    variant="contained"
                    color="primary" // You can adjust the color based on your design
                    style={{
                        marginTop: '20px', // Add some spacing from the elements above
                        borderRadius: '10px', // Add rounded corners for a modern look
                    }}
                    onClick={()=>LogoutSession()}
                    >
                        Log out
                    </Button>

                </Stack>

            </Grid>
        </Grid>
    
        </div>
        :
        <ProfileSettings />
    }
    </div>
)
}

export default Settings