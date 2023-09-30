import React, { useState } from 'react';
import { GoogleOAuthProvider,GoogleLogin  } from '@react-oauth/google';
import jwt_decode from 'jwt-decode'
import './UserDetail.css';
import Loginimg from "../images/register.svg";
import { dark } from 'react-syntax-highlighter/dist/esm/styles/hljs';
function UserDetail({handleUserDetail,isAuthenticated,userInfo}) {
  console.log("sisisisi",isAuthenticated);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
  const [isSignup, setIsSignup] = useState(false);

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
handleUserDetail(isSignup,username,password,email,null,null,"632050271544-7vr7fs6kss02oakf95q4v6f25rur7oqt.apps.googleusercontent.com");
  };
  return (
    <div className='userdetail'>

 {isAuthenticated ? ( <div className='user-panel'>
  <div className='odiv'>
        <div  className='odiv'>Username:{userInfo}</div>
            <div  className='odiv'>Usage:</div>
            <div  className='odiv'>Upgrade</div>
              <div  className='odiv'>Logout</div>
            </div>
      </div>):

    (<div className='user-panel'>
        <div className="loginimg">
        <img src={Loginimg} alt="User Avatar" />
      </div>
                <div className="auth-container">
<GoogleOAuthProvider clientId="632050271544-7vr7fs6kss02oakf95q4v6f25rur7oqt.apps.googleusercontent.com">
    <GoogleLogin
  onSuccess={credentialResponse => {
    const userdetail=jwt_decode(credentialResponse.credential)
    console.log(userdetail);
handleUserDetail(false,userdetail["given_name"],userdetail["family_name"],userdetail["email"],userdetail["aud"],userdetail["iss"],"632050271544-7vr7fs6kss02oakf95q4v6f25rur7oqt.apps.googleusercontent.com");

  }}
  onError={() => {
    console.log('Login Failed');
  }}
/></GoogleOAuthProvider>
</div>
<div class="horizontal-line"></div>
         <div className="login-container">
      <h2>{isSignup ? 'Sign Up' : 'Login'}</h2>
      <form onSubmit={handleLoginButtonClick}>

        {isSignup ? (<div className="form-group">
          <label htmlFor="email">Email-Id</label>
          <input
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
        {isSignup ?(<p class="punder">Already have an account? <a onClick={() => setIsSignup(!isSignup)} class="link-danger">Sign in</a></p>)
         : (<p className="punder">Don't have an account? <a onClick={() => setIsSignup(!isSignup)} class="link-danger">Register</a></p>)
         }
    </div>


</div>)}

    </div>
  )
}

export default UserDetail