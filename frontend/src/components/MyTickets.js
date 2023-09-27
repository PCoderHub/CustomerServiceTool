import { Button, Card } from "@mui/material";
import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import axios from "../axiosConfig";
import { addConcernInfo } from "../redux/concernSlicer";
import Header from "./Header";
import './MyTickets.css';


const MyTickets = () => {

    const [myConcerns, setMyConcerns] = useState();
    const dispatch = useDispatch();
    const navigate = useNavigate();

    // to get legged in user data from store
    const userData = useSelector(
        (state) => state?.user?.user
    );

    // to get all tickets raised by current user
    const getMyConcerns = () => {
        const response = axios.get('/concerns', {
            params: {userName: userData.userName}
        }).then((res) => setMyConcerns(res.data)).catch((err) => console.log(err));
    }

    useEffect(() => {
        getMyConcerns();
    }, []);

    const handleEdit = (myconcern) => {
        dispatch(addConcernInfo(myconcern));
        navigate('/edit');
    }

    const handleDelete = (myconcern) => {
        const response = axios.delete(`/concerns/${myconcern.id}`).then((res) => {
            console.log(res);
            getMyConcerns();
        }).catch((err) => console.log(err));
    }

    return <div>
        <Header />
        <h1>My Tickets</h1>
        {myConcerns?.length>0 && myConcerns.map((myconcern) => {
            return (
                <Card className="concerns">
                    <p className="p">Email: {myconcern.email}</p>
                    <p className="p">Agent: {myconcern.agent}</p>
                    <p className="p">Type: {myconcern.concern}</p>
                    <p className="p">Subject: {myconcern.subject}</p>
                    {myconcern.description != null && <p className="p">Description: {myconcern.description}</p>}
                    <Button onClick={() => handleEdit(myconcern)}>Edit</Button>
                    <Button onClick={() => handleDelete(myconcern)}>Delete</Button>
                </Card>
            );
        })}
    </div>
}

export default MyTickets;