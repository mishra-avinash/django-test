/**
 * Created by avinash on 19.05.17.
 */
var React = require('react')
var ReactDOM = require('react-dom')
import React, {Component} from 'react';
// import { Router, Route,browserHistory} from 'react-router'
import {BrowserRouter, Route} from 'react-router-dom';
import FormContainer from '../containers/formContainer';
import TableContainer from '../containers/tableContainer';




ReactDOM.render(
    <BrowserRouter>
        <div>
        <Route path="/create" component={FormContainer}/>
        <Route path="/" component={TableContainer}/>

        </div>
    </BrowserRouter>,
    document.getElementById('container')
);