import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { suggestedRecipe } from './pages/suggestedRecipe';

export const Routes = () => {
    return (
        <Router>
            <Switch>
                <Route path = "/suggestedRecipe">
                    <suggestedRecipe />
                </Route>
            </Switch>
        </Router>
    )
}