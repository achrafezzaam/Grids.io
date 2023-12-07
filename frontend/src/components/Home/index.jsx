import "./index.css";
import AddGrid from "../../assets/add_grid.png";
import AddComponent from "../../assets/add_component.png";
import UpdateGrid from "../../assets/update_grid.png";

const Home = () => {
  return (
	<div className="container home-page">
    <div className="hero">
    	<h1>Grids.io</h1>
	<p>Monitore your electrical grid</p>
    </div>
    <div className="sectn">
        <h3>Grid creation</h3>
        <p>This feature give you the possibility to create a grid and label it with a name</p>
	<img src={AddGrid} />
    </div>
    <div className="sectn">
        <h3>Component Creation</h3>
        <p>This feature allows you to create a component and assign it directly to the desired Grid</p>
	<img src={AddComponent} />
    </div>
    <div className="sectn">
        <h3>Grid Update</h3>
        <p>You'll be able to update a grid</p>
	<img src={UpdateGrid} />
    </div>
    <div className="about">
	<h3>About</h3>
	<p>This project was inspired by a job opening I saw few months ago. I got really hooked by the idea. So here come my project.</p>
	<h4>Team members</h4>
	<a href="https://github.com/achrafezzaam/">-&gt; Achraf Ezzaam</a>
	<h4>Project repository</h4>
	<a href="https://github.com/achrafezzaam/Grids.io">-&gt; Link</a>
	<iframe width="420" height="315" src="https://www.youtube.com/embed/_jj0GZdAcOw" allowFullScreen>
        </iframe>
    </div>
	</div>
  );
}

export default Home
