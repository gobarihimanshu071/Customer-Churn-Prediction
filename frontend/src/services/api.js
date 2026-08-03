import axios from "axios";

const API = axios.create({
    baseURL: "http://churn-alb-1763293995.us-east-2.elb.amazonaws.com"
});

export default API;