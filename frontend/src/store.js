import { configureStore, combineReducers } from "@reduxjs/toolkit";
import concernReducer from "./redux/concernSlicer";
import userReducer from "./redux/userSlicer";

const rootReducer = combineReducers({
    user: userReducer,
    concern: concernReducer
});

export default configureStore({
    reducer: rootReducer,
});