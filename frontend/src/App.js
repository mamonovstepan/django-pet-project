import axios from 'axios'
import React from 'react';

class App extends React.Component {
    state = {details: [],}
    
    componentDidMount() {
        let data;
        axios.get('http://localhost:8000/crm-api/')
        .then(res => {
            data = res.data;
            this.setState({
                details: data
            });
        })
    .catch(err => { })
    }
    render() {
        return(
            <div>
            <header><h1>Данные полученные из Django</h1></header>
            <hr></hr>
            {this.state.details.map((output, id) => (
                <div>
                    <h1>{output.first_name} {output.last_name}</h1>
                    <h1></h1>
                </div>
            ))}
            </div>
        )
    }    
}

export default App;
