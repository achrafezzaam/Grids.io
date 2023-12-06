import "./index.css";

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
    </div>
    <div className="sectn">
        <h3>Component Creation</h3>
        <p>This feature allows you to create a component and assign it directly to the desired Grid</p>
    </div>
    <div className="sectn">
        <h3>Grid Update</h3>
        <p>You'll be able to update a grid</p>
    </div>
    <div className="about">
	<h3>About</h3>
	<p>This project was inspired by a job opening I saw few months ago. I got really hooked by the idea. So here come my project.</p>
	<h4>Team members</h4>
	<a href="https://github.com/achrafezzaam/">-&gt; Achraf Ezzaam</a>
	<h4>Project repository</h4>
	<a href="https://github.com/achrafezzaam/Grids.io">-&gt; Link</a>
    </div>
	</div>
  );
}

export default Home
