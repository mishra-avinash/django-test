
/**
 * Created by avinash on 19.05.17.
 */
var React = require('react')
import React, {Component} from 'react';



var TableContainer = React.createClass({
    //making ajax call to get data from server
    loadEmployeeDetails: function () {
        $.ajax({
            url: 'http://127.0.0.1:8000/employee/',
            datatype: 'json',
            cache: false,
            success: function (data) {
                this.setState({data: data.results});
            }.bind(this)
        })
    },
    //setting up initial state
    getInitialState: function () {
        return {
            data: []
        };
    },
    componentDidMount(){
        this.loadEmployeeDetails();
    },
    //showResult Method
    showResult: function (response) {

        this.setState({
            data: response
        });
    },
        render: function () {
        this.loadEmployeeDetails()
            console.log(this.state.data)
        var result = this.state.data.map(function (result, index) {
            return <ResultItem key={index} user={ result }/>
        });
        return (
            <div className="row">
                <div className="col-md-12">
                    <table className="table table-bordered">
                        <thead>
                        <tr>
                            <th className="col-md-4">Full Name</th>
                            <th >Phone Number</th>
                            <th>Company</th>
                            <th>Department</th>
                            <th>Occupation</th>

                        </tr>
                        </thead>
                        <tbody>
                        {result}
                        </tbody>
                    </table>
                </div>
            </div>
        );
    }
});


var ResultItem = React.createClass({
    render: function () {
        var camper = this.props.user;
        return (
            <tr >
                <td>{camper.full_name}</td>
                <td>{camper.phone_number}</td>
                <td>{camper.company}</td>
                <td>{camper.department}</td>
                <td>{camper.occupation}</td>
            </tr>
        );
    }
});

export default TableContainer;
