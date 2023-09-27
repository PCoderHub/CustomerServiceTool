import { createSlice } from "@reduxjs/toolkit"

const initialState = {
    concern: {},
}

const concernSlicer = createSlice({
    name: 'concern',
    initialState,
    reducers: {
        addConcernInfo: (state, action) => {
            state.concern = {...action?.payload}
            console.log(state.concern);
        },
    },
});

export const {addConcernInfo} = concernSlicer.actions;
export default concernSlicer.reducer;