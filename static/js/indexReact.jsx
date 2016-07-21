var BandComponent = React.createClass({

    getInitialState: function(){
      return {customText: "fuck"};
    },
    customClickFuntion: function(){
      this.setState({customText:"click"});
    },
    render: function(){

        return(
            <div className="testClass" >
                <h1>{this.state.customText}</h1>
                <button onClick={this.customClickFuntion}>click me</button>

            </div>
        )
    }
});


React.render(
    <BandComponent />,
    document.getElementById("band_component")
)