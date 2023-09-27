import { Button, Card, FormControl, FormControlLabel, InputLabel, MenuItem, Radio, RadioGroup, Select, TextareaAutosize, TextField } from "@mui/material";
import React, { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import axios from "../axiosConfig";
import Header from "./Header";
import './Home.css';

const Home = () => {

    const [email, setEmail] = useState('');
    const [agent, setAgent] = useState('');
    const [concernType, setConcernType] = useState('');
    const [subject, setSubject] = useState('');
    const [description, setDescription] = useState('');
    const [agents, setAgents] = useState();
    const [error, setError] = useState(false);

    // to get user added in store
    const userData = useSelector(
        (state) => state?.user?.user
    );

    //to get agent usernames from backend
    const getAgents = () => {
        const response = axios.get('/register/agent').then((res) => setAgents(res.data)).catch((err) => console.log(err));
    }

    useEffect(() => {
        getAgents();
    });

    const handleSubmit = (e) => {
        e.preventDefault();

        if (email.length == 0 || agent == '' || concernType == '' || subject.length==0 || description.length == 0) {
            setError(true);
        }
        if (email&&agent&&concernType&&subject) {
            const concernData = {
                userName: userData.userName,
                email: email,
                agent: agent,
                concernType: concernType,
                subject: subject,
                description: description
            }
    
            const response = axios.post('concerns', concernData).then((res) => console.log(res)).catch((err) => console.log(err));
            setEmail('');
            setAgent('');
            setConcernType('');
            setSubject('');
            setDescription('');
        }
        
    }

    return <div>
        <Header title="My Tickets" />
        <Card className="card">
            <h4>Any concerns with your travel? <br/>Raise a ticket here and your agent will get back to you <br/>with a solution within 24 hours.</h4>
            <form className="form" onSubmit={handleSubmit}>
            <TextField style={{width: 250}} className="field" label="Email" variant="standard" value={email} onChange={(e) => setEmail(e.target.value)} required />
            <FormControl className="field" sx={{m:1, minWidth:250}}>
                <InputLabel id="agent">Your Agent</InputLabel>
                <Select labelId="agent" id="agentname" value={agent} onChange={(e) => setAgent(e.target.value)}>
                    <MenuItem value=""><em>None</em></MenuItem>
                    {agents?.length>0 && agents.map((ag) => {
                        return (
                            <MenuItem value={ag.userName}>{ag.userName}</MenuItem>
                        );
                    })}
                </Select>
            </FormControl>
            {error&&agent.length<=0 ? <label style={{color: 'red'}}>Field cannot be empty</label> : ""}
            <FormControl className="field">
                <RadioGroup name="concern" value={concernType} onChange={(e) => setConcernType(e.target.value)}>
                    <FormControlLabel value="complaint" control={<Radio />} label="Complaint" />
                    <FormControlLabel value="query" control={<Radio />} label="Query" />
                </RadioGroup>
            </FormControl>
            {error&&concernType.length<=0 ? <label style={{color: 'red'}}>Field cannot be empty</label> : ""}
            <TextField style={{width: 250}} className="field" label="Subject" variant="outlined" value={subject} onChange={(e) => setSubject(e.target.value)} required />
            {concernType == "query" ? <div className="field">
            <TextareaAutosize style={{width: 250}} minRows={4} placeholder="Description" value={description} onChange={(e) => setDescription(e.target.value)} required />
            </div> : <div className="field">
            </div>}
            <Button className="field" variant="contained" color="primary" type="submit">Raise Ticket</Button>
            </form>
        </Card>
    </div>
}

export default Home;