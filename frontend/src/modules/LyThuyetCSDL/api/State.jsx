import api from "./CauHinh";

const StateApi = {

    fetchState: () =>
        api.get("/state"),

};

export default StateApi;