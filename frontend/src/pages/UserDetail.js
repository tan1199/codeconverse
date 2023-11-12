import React, { useState,useEffect  } from 'react';
import { GoogleOAuthProvider,GoogleLogin  } from '@react-oauth/google';
import jwt_decode from 'jwt-decode'
import './UserDetail.css';
function UserDetail({handleUserDetail,isAuthenticated}) {
  console.log("sisisisi",isAuthenticated);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
  const [isSignup, setIsSignup] = useState(false);
    const [googleCID, setGoogleCID] = useState(false);

  const handleGoogleLogin = () => {
     console.log("hmhmhm ")
    fetch("http://localhost:8000/googlecidtoken", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("glgglgl ",data.googleCID)
              setGoogleCID(data.googleCID)

      })
      .catch((error) => {
        console.error("Error:", error);
      })

  };

   useEffect(() => {
    // This will be called when the component mounts
    handleGoogleLogin();
  }, [])
    const handleLoginButtonClick = (e) => {
      e.preventDefault(); 
    // toast.success('Success Notification !', {
    //         position: toast.POSITION.TOP_RIGHT
    //     });
    //     toast.dark('Login Successful!', {
    //   position: 'top-center', // Center the toast at the top of the screen
    //   autoClose: 500, // Automatically close the toast after 2 seconds
    //   hideProgressBar: true, // Hide the progress bar
    // });
    //         toast.error('Login Successful!', {
    // position: toast.POSITION.TOP_CENTER,
    //   autoClose: 500, // Automatically close the toast after 2 seconds
    //   hideProgressBar: true, // Hide the progress bar
    // });

console.log("lpjl");
handleUserDetail(isSignup,username,password,email,null,null,googleCID);
  };
  return (
    <div className='userdetail'style={{ backgroundImage: `url(/124.jpg)`,backgroundSize: 'cover',
        backgroundRepeat: 'no-repeat', }}>

 {isAuthenticated ? ( <div className='about-info'>
For security reasons, this page has expired.
      </div>):

    (<div className='user-panel' >
        {/* <div className="loginimg">
        <img src={Loginimg} alt="User Avatar" />
      </div> */}
                <div className="auth-container">
<GoogleOAuthProvider clientId={googleCID}>
    <GoogleLogin
  onSuccess={credentialResponse => {
    const userdetail=jwt_decode(credentialResponse.credential)
    console.log(userdetail);
handleUserDetail(false,userdetail["given_name"],userdetail["family_name"],userdetail["email"],userdetail["aud"],userdetail["iss"],googleCID);

  }}
  onError={() => {
    console.log('Login Failed');
  }}
/></GoogleOAuthProvider>
</div>
<div className="horizontal-line"></div>
         <div className="login-container">
      <h2>{isSignup ? 'Sign Up' : 'Login'}</h2>
      <form onSubmit={handleLoginButtonClick}>

        {isSignup ? (<div className="form-group">
          <label htmlFor="email">Email-Id</label>
          <input
            autoFocus
            type="text"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>) : (<div></div>)}
        <div className="form-group">
          <label htmlFor="username">Username</label>
          <input
            autoFocus
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button className='signbtn'>
          {isSignup ? 'Sign Up' : 'Login'}
        </button>
      </form>
        {isSignup ?(<p className="punder">Already have an account? <a onClick={() => setIsSignup(!isSignup)} className="link-danger">Sign in</a></p>)
         : (<p className="punder">Don't have an account? <a onClick={() => setIsSignup(!isSignup)} className="link-danger">Register</a></p>)
         }
    </div>


</div>)}

    </div>
  )
}

export default UserDetail