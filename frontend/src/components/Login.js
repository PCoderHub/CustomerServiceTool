import { Card, TextField, Button } from "@mui/material";
import axios from './../axiosConfig';
import React, {useState} from "react";
import { Link, useNavigate } from "react-router-dom";
import './Login.css';
import { useDispatch } from "react-redux";
import { addUserInfo } from "../redux/userSlicer";

const Login = () => {

    const [userName, setUserName] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();
    const dispatch = useDispatch();

    const handleSubmit = (e) => {
        e.preventDefault();
        
        const userData = {
            userName: userName,
            password: password
        }

        const response = axios.post('/login', userData).then((res) => {
            dispatch(addUserInfo(userData));
            (res.data.userType == "agent") ? navigate('/agent') : navigate('/home');
        }).catch((err) => alert(err.response.data.error));
    }

    return <Card className="container">
        <h1>Login</h1>
        <form className="form" onSubmit={handleSubmit}>
            <TextField className="field" label="Username" variant="standard" value={userName} onChange={(e) => setUserName(e.target.value)} required />
            <TextField className="field" label="Password" variant="standard" type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
            <Button className="field" variant="contained" color="primary" type="submit">Login</Button>
            <p className="field">Not registered? <span><Link to="/">Sign Up</Link></span></p>
        </form>
        </Card>
}

export default Login;