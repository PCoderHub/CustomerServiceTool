import { Button, Card, TextareaAutosize, TextField } from "@mui/material";
import React, { useState } from "react";
import { useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import axios from "../axiosConfig";
import Header from "./Header";

const UpdateTicket = () => {

    const myconcern = useSelector(
        (state) => state?.concern?.concern
    );
    const navigate = useNavigate();
    const [email, setEmail] = useState(myconcern.email);
    const [agent, setAgent] = useState(myconcern.agent);
    const [subject, setSubject] = useState(myconcern.subject);
    const [description, setDescription] =useState(myconcern?.description);

    const handleSubmit = (e) => {
        e.preventDefault();

        let updatedTicket = {
            email: email,
            agent: agent,
            concern: myconcern.concern,
            subject: subject,
            description: description
        }

        const response = axios.put(`/concerns/${myconcern.id}`, updatedTicket).then((res) => console.log(res)).catch((err) => console.log(err));
        navigate(-1);
    }


    return <div>
        <Header />
        <h1>Edit Ticket</h1>
        <Card className="card">
            <form className="form" onSubmit={handleSubmit}>
            <TextField style={{width: 250}} className="field" label="Email" variant="standard" value={email} onChange={(e) => setEmail(e.target.value)} />
            <TextField style={{width: 250}} className="field" label="Your Agent" variant="standard" value={agent} onChange={(e) => setAgent(e.target.value)} />
            <TextField style={{width: 250}} className="field" label="Subject" variant="outlined" value={subject} onChange={(e) => setSubject(e.target.value)} />
            {myconcern.concern == "query" ? <div className="field">
            <TextareaAutosize style={{width: 250}} minRows={4} placeholder="Description" value={description} onChange={(e) => setDescription(e.target.value)} />
            </div> : <div className="field">
            </div>}
            <Button className="field" variant="contained" color="primary" type="submit">Update Ticket</Button>
            </form>
        </Card>
    </div>
}

export default UpdateTicket;