import { Button } from "@mui/material";
import React from "react";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import { addUserInfo } from "../redux/userSlicer";
import './Header.css';

const Header = (props) => {

    const navigate = useNavigate();
    const dispatch = useDispatch();

    const handleClick = () => {
        navigate('/mytickets');
    }

    const handleLogOut = () => {
        navigate('/login');
        dispatch(addUserInfo({}));
    }

    return <div className="header">
        <div className="header-left">
            <h3>TravelAgent Customer Service Tool</h3>
        </div>
        <div className="header-right">
            {(props?.title) && <Button className="button" variant="contained" color="secondary" onClick={handleClick}>{props.title}</Button>}
            <Button className="button" variant="contained" color="secondary" onClick={handleLogOut}>logout</Button>
        </div>     
    </div>
}

export default Header;