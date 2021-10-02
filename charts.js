import React, {Component} from 'react'; /* importing Component package too */

// following
// https://www.npmjs.com/package/react-chartjs-2

// import { Bar, Line, Pie } from 'react-chartjs-2';
import { Bar} from 'react-chartjs-2';

class Chart extends Component{

    // creating an initial state where we will keep all our data
    // this func will run when components are initialised
    constructor(props){
        // to set state, call super func and pass in props
        super(props);
        this.state = {
            chartData:props.chartData
        }
    }

    static defaultProps = {
        displayTitle:true,
        displayeLegend:true,
        legendPosition:'right'
    }

    // in react, whenever we want to open to the screen we use render fun
    render(){
        return(
            <div className="chart">
                <Bar
                    data={this.state.chartData}
                    options={{ 
                        title:{
                            display:this.props.displayTitle,
                            text:'Doses Bar Graph in'+this.props.location,
                            fontSize:25
                        },
                        legend:{
                            display:this.props.displayeLegend,
                            position:this.props.legendPosition
                        }
                    }}
                />
                {/* <Line
                    data={this.state.chartData}
                    options={{ 
                        title:{
                            display:this.props.displayTitle,
                            text:'Doses Bar Graph in'+this.props.location,
                            fontSize:25
                        },
                        legend:{
                            display:this.props.displayeLegend,
                            position:this.props.legendPosition
                        }
                    }}
                />
                <Pie
                    data={this.state.chartData}
                    options={{ 
                        title:{
                            display:this.props.displayTitle,
                            text:'Doses Bar Graph in'+this.props.location,
                            fontSize:25
                        },
                        legend:{
                            display:this.props.displayeLegend,
                            position:this.props.legendPosition
                        }
                    }}
                /> */}
            </div>
        )
    }
}

// to send this class to App.js
export default Chart;