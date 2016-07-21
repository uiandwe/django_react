var bands = [
    {name: "band1", "image": "http://www.gifpng.com/300/?text=한국어&line-height=2.5"},
{name: "band2", "image": "http://www.gifpng.com/300/?text=English&line-height=2.5"},
{name: "band3", "image": "http://www.gifpng.com/300/?text=한국어&line-height=2.5"}
]


var BandComponent = React.createClass({

    getInitialState: function(){
      return {customText: "test"};
    },
    customClickFuntion: function(){
      this.setState({customText:"click"});
    },
    render: function(){

        return(
            <div className="testClass" >
                <h1>{this.state.customText}</h1>
                <button onClick={this.customClickFuntion}>click me</button>
                {bands.map(function(band){
                    return(
                    <Band name={band.name} image={band.image} />
                    )
                })}

            </div>
        )
    }
});

var Band = React.createClass({
    render: function(){
        return (
            <div>
                <h2>{this.props.name}</h2>
                <img src={this.props.image} />
            </div>
        )
    }
});

React.render(
    <BandComponent bands={bands} />,
    document.getElementById("band_component")
)