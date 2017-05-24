//  * Created by avinash on 20.05.17.


import React, {Component} from 'react';
import SingleInput from '../components/SingleInput';

class FormContainer extends Component {
    constructor(props) {
        super(props);
        this.state = {
            fullName: '',
            phoneNumber: 0,
            company: '',
            department: '',
            occupation: ''
        };
        this.handleFormSubmit = this.handleFormSubmit.bind(this);
        this.handleClearForm = this.handleClearForm.bind(this);
        this.handleFullNameChange = this.handleFullNameChange.bind(this);
        this.handlePhoneNumber = this.handlePhoneNumber.bind(this);
        this.handleCompany = this.handleCompany.bind(this);
        this.handleDepartment = this.handleDepartment.bind(this);
        this.handleOccupation = this.handleOccupation.bind(this)
    }


    handleFullNameChange(e) {
        this.setState({fullName: this.state.fullName});
    }

    handlePhoneNumber(e) {
        this.setState({phoneNumber: this.state.phoneNumber});
    }

    handleCompany(e) {
        this.setState({company: this.state.company});
    }

    handleDepartment(e) {
        this.setState({department: this.state.department});
    }

    handleOccupation(e) {
        this.setState({occupation: this.state.occupation});
    }

    handleClearForm(e) {
        // e.preventDefault();
        this.setState({
            fullName: '',
            phoneNumber: 0,
            company: '',
            department: '',
            occupation: ''
        });
    }

    handleFormSubmit(e) {
        // e.preventDefault();

        const formPayload = {
            fullName: this.state.fullName,
            phoneNumber: this.state.phoneNumber,
            company: this.state.company,
            department: this.state.department,
            occupation: this.state.occupation
        };

        fetch('http://127.0.0.1:8000/employee/', {
            method: 'POST',
            body: JSON.stringify({
            fullName: this.state.fullName,
            phoneNumber: this.state.phoneNumber,
            company: this.state.company,
            department: this.state.department,
            occupation: this.state.occupation
            })
        })

        console.log('Send this in a POST request:', formPayload);
        this.handleClearForm(e);
    }

    render() {
        return (
            <form className="container" onSubmit={this.handleFormSubmit}>
                <h5>Employee Registration Form</h5>
                <SingleInput
                    inputType={'text'}
                    title={'Full name'}
                    name={'name'}
                    controlFunc={this.handleFullNameChange}
                    content={this.state.fullName}
                    placeholder={'Type first and last name here'}/>
                <SingleInput
                    inputType={'company'}
                    title={'company'}
                    name={'company'}
                    controlFunc={this.handleCompany()}
                    content={this.state.company}
                    placeholder={'Type company name here'}/>

                <SingleInput
                    inputType={'number'}
                    title={'phone number'}
                    name={'phoneNumber'}
                    controlFunc={this.handlePhoneNumber}
                    content={this.state.phoneNumber}
                    placeholder={'Enter phone number here '}/>
                <SingleInput
                    inputType={'text'}
                    title={'Department name'}
                    name={'department'}
                    controlFunc={this.handleDepartment()}
                    content={this.state.department}
                    placeholder={'Type department name here'}/>
                <SingleInput
                    inputType={'text'}
                    title={'occupation'}
                    name={'occupation'}
                    controlFunc={this.handleOccupation()}
                    content={this.state.occupation}
                    placeholder={'Type occupation here'}/>
                <input
                    type="submit"
                    className="btn btn-primary float-right"
                    value="Submit"/>
                <button
                    className="btn btn-link float-left"
                    onClick={this.handleClearForm}>Clear form
                </button>
            </form>
        );
    }
}

export default FormContainer;
