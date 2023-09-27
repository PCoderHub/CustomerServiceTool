import { Button, Card, Radio, TextField } from "@mui/material";
import { FormControl, RadioGroup, FormControlLabel } from "@mui/material";
import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import './Register.css';
import axios from './../axiosConfig';

const Register = () => {

    const [userName, setUserName] = useState('');
    const [password, setPassword] = useState('');
    const [userType, setUserType] = useState('');
    const [error, setError] = useState(false);
    const navigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault();
        if (userName.length == 0 || password.length == 0 || userType == '') {
            setError(true);
        }
        if (userName&&password&&userType) {
            let userData = {
                userName: userName,
                password: password,
                userType: userType
            }
    
            const response = axios.post('/register', userData).then((res) => navigate('/login')).catch((err) => alert(err.response.data.error));
        }
        /*if(userName != "" && password != "") {
            navigate('/login');
        }*/
    }

    return <Card className="container">
        <h1>Register</h1>
        <form className="form" onSubmit={handleSubmit}>
            <TextField label="Username" variant="standard" value={userName} onChange={(e) => setUserName(e.target.value)} required />
            <TextField label="Password" variant="standard" value={password} type="password" onChange={(e) => setPassword(e.target.value)} required />
            <FormControl>
                <RadioGroup aria-label="usertype" name="usertype" value={userType} onChange={(e) => setUserType(e.target.value)}>
                    <FormControlLabel value="agent" control={<Radio />} label="Agent"/>
                    <FormControlLabel value="customer" control={<Radio />} label="Customer"/>
                </RadioGroup>
            </FormControl>
            {error && userType=='' ? <label style={{color: 'red'}}>Field cannot be empty</label> : ""}
            <Button variant="contained" color="primary" type="submit">Register</Button>
        </form>
        <p>Already Registered? <span><Link to="/login">Sign In</Link></span></p>
    </Card>
}

export default Register;