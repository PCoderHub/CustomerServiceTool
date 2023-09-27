import { Card } from "@mui/material";
import React, { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import axios from "../axiosConfig";
import Header from "./Header";
import './AgentHome.css';

const AgentHome = () => {

    const [concerns, setConcerns] = useState();
    const userData = useSelector(
        (state) => state?.user?.user
    );

    // to get concerns from backend
    const getConcerns = () => {
        const response = axios.get('/concerns').then((res) => setConcerns(res.data)).catch((err) => console.log(err));
    }

    useEffect(() => {
        getConcerns();
    }, []);

    return <div>
        <Header />
        <h1>Hi {userData.userName}! Welcome! <br /> Inform the user via email once the issue is resolved.</h1>
        {concerns?.length>0 && concerns.map((issue) => {
            return (
                <Card className="cards">
                    <p>Username : {issue.userName}</p>
                    <p>Email : {issue.email}</p>
                    <p>Agent : {issue.agent}</p>
                    <p>Priority : {issue.priority}</p>
                    <p>SLA : {issue.concernType}</p>
                    <p>Subject : {issue.subject}</p>
                    {issue.description != null && <p>Description : {issue.description}</p>}
            </Card>
            );
        })}
    </div>
}

export default AgentHome;