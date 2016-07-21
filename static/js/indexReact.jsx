var BandComponent = React.createClass({

    render: function(){

        return(
            <div className="testClass" >

                <div>test</div>
                <div>test</div>
                <div>test</div>

                </div>
        )
    }
});


React.render(
    <BandComponent />,
    document.getElementById("band_component")
)